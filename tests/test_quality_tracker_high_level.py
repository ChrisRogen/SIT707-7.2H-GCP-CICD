import time
from collections import Counter

import pytest

from app import create_app
from app.services import (
    calculate_quality_summary,
    create_test_record,
    get_all_test_records,
    validate_test_record,
)


@pytest.fixture()
def client():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    return app.test_client()


# RIGHT: Valid input should be accepted.
def test_right_valid_record_is_accepted():
    # Arrange
    test_name = "Cloud Build pipeline test"
    module_name = "CI Pipeline"
    status = "Pass"

    # Act
    result = validate_test_record(test_name, module_name, status)

    # Assert
    assert result["valid"] is True
    assert result["message"] == "Valid test record."


# BOUNDARY: Minimum meaningful one-character values should be accepted.
def test_boundary_minimum_valid_text_values_are_accepted():
    # Arrange
    test_name = "A"
    module_name = "B"
    status = "Pass"

    # Act
    result = validate_test_record(test_name, module_name, status)

    # Assert
    assert result["valid"] is True


# BOUNDARY + ERROR: Whitespace-only values should be rejected.
# This test supports the TDD red stage because the original implementation
# accepts whitespace-only input until validation is improved.
def test_boundary_whitespace_only_test_name_is_rejected():
    # Arrange
    test_name = "   "
    module_name = "Authentication"
    status = "Pass"

    # Act
    result = validate_test_record(test_name, module_name, status)

    # Assert
    assert result["valid"] is False
    assert "Test name is required" in result["message"]


# ERROR: Invalid status values should not be accepted.
def test_error_invalid_status_is_rejected():
    # Arrange
    test_name = "Login validation"
    module_name = "Authentication"
    status = "Pending"

    # Act
    result = validate_test_record(test_name, module_name, status)

    # Assert
    assert result["valid"] is False
    assert "Status must be Pass, Fail, or Blocked" in result["message"]


# INVERSE: Adding one Pass record should increase total and pass count.
def test_inverse_created_pass_record_changes_summary_counts():
    # Arrange
    before_records = get_all_test_records()
    before_summary = calculate_quality_summary(before_records)

    # Act
    create_test_record("Deployment smoke test", "Cloud Run", "Pass")
    after_records = get_all_test_records()
    after_summary = calculate_quality_summary(after_records)

    # Assert
    assert after_summary["total"] == before_summary["total"] + 1
    assert after_summary["passed"] == before_summary["passed"] + 1


# CROSS-CHECK: Summary result is checked against independent manual counting.
def test_cross_check_summary_matches_independent_counter():
    # Arrange
    records = [
        {"status": "Pass"},
        {"status": "Fail"},
        {"status": "Pass"},
        {"status": "Blocked"},
        {"status": "Pass"},
    ]
    independent_count = Counter(record["status"] for record in records)

    # Act
    summary = calculate_quality_summary(records)

    # Assert
    assert summary["total"] == len(records)
    assert summary["passed"] == independent_count["Pass"]
    assert summary["failed"] == independent_count["Fail"]
    assert summary["blocked"] == independent_count["Blocked"]
    assert summary["pass_rate"] == round((independent_count["Pass"] / len(records)) * 100, 2)


# FUNCTIONAL / INTEGRATION: Dashboard form should accept valid input and display it.
def test_integration_dashboard_form_adds_valid_record(client):
    # Arrange
    form_data = {
        "test_name": "Artifact Registry image push test",
        "module_name": "GCP Artifact Registry",
        "status": "Pass",
    }

    # Act
    response = client.post("/dashboard", data=form_data, follow_redirects=True)

    # Assert
    assert response.status_code == 200
    assert b"Artifact Registry image push test" in response.data
    assert b"GCP Artifact Registry" in response.data


# ERROR / VALIDATION: Dashboard should display an error for invalid form input.
def test_error_dashboard_form_rejects_missing_module_name(client):
    # Arrange
    form_data = {
        "test_name": "Cloud Run deployment verification",
        "module_name": "",
        "status": "Blocked",
    }

    # Act
    response = client.post("/dashboard", data=form_data, follow_redirects=True)

    # Assert
    assert response.status_code == 200
    assert b"Module name is required" in response.data


# API TEST: Health endpoint should return correct HTTP and JSON values.
def test_api_health_endpoint_contract(client):
    # Arrange
    expected_status = "healthy"
    expected_service = "SIT707 Quality Tracker"

    # Act
    response = client.get("/health")
    data = response.get_json()

    # Assert
    assert response.status_code == 200
    assert data["status"] == expected_status
    assert data["service"] == expected_service


# PERFORMANCE: Summary calculation should handle a larger dataset efficiently.
def test_performance_summary_handles_large_dataset_quickly():
    # Arrange
    records = (
        [{"status": "Pass"} for _ in range(5000)]
        + [{"status": "Fail"} for _ in range(3000)]
        + [{"status": "Blocked"} for _ in range(2000)]
    )

    # Act
    start_time = time.perf_counter()
    summary = calculate_quality_summary(records)
    duration = time.perf_counter() - start_time

    # Assert
    assert summary["total"] == 10000
    assert summary["passed"] == 5000
    assert summary["failed"] == 3000
    assert summary["blocked"] == 2000
    assert summary["pass_rate"] == 50.0
    assert duration < 1.0

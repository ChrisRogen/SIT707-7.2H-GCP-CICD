from app.services import (
    validate_test_record,
    calculate_quality_summary,
    create_test_record,
)

def test_validate_test_record_accepts_valid_data():
    result = validate_test_record("Login test", "Authentication", "Pass")
    assert result["valid"] is True
    assert result["message"] == "Valid test record."

def test_validate_test_record_rejects_missing_test_name():
    result = validate_test_record("", "Authentication", "Pass")
    assert result["valid"] is False
    assert "Test name is required" in result["message"]

def test_validate_test_record_rejects_missing_module_name():
    result = validate_test_record("Login test", "", "Pass")
    assert result["valid"] is False
    assert "Module name is required" in result["message"]

def test_validate_test_record_rejects_invalid_status():
    result = validate_test_record("Login test", "Authentication", "Unknown")
    assert result["valid"] is False
    assert "Status must be Pass, Fail, or Blocked" in result["message"]

def test_calculate_quality_summary_counts_status_values():
    records = [
        {"status": "Pass"},
        {"status": "Pass"},
        {"status": "Fail"},
        {"status": "Blocked"},
    ]

    summary = calculate_quality_summary(records)

    assert summary["total"] == 4
    assert summary["passed"] == 2
    assert summary["failed"] == 1
    assert summary["blocked"] == 1
    assert summary["pass_rate"] == 50.0

def test_calculate_quality_summary_handles_empty_records():
    summary = calculate_quality_summary([])

    assert summary["total"] == 0
    assert summary["passed"] == 0
    assert summary["failed"] == 0
    assert summary["blocked"] == 0
    assert summary["pass_rate"] == 0

def test_create_test_record_returns_new_record():
    record = create_test_record("Cloud Build test", "CI Pipeline", "Pass")

    assert record["test_name"] == "Cloud Build test"
    assert record["module_name"] == "CI Pipeline"
    assert record["status"] == "Pass"
    assert "created_at" in record

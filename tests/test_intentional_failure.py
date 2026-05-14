def test_intentional_ci_failure_for_documentation():
    # Arrange
    expected_pass_rate = 80.0
    actual_pass_rate = 50.0

    # Act
    result = actual_pass_rate

    # Assert
    assert result == expected_pass_rate

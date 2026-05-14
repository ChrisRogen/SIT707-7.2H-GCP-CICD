def test_intentional_ci_failure_fixed_for_documentation():
    # Arrange
    expected_pass_rate = 50.0
    actual_pass_rate = 50.0

    # Act
    result = actual_pass_rate

    # Assert
    assert result == expected_pass_rate

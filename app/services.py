from datetime import datetime

_test_records = [
    {
        "test_name": "Login validation test",
        "module_name": "Authentication",
        "status": "Pass",
        "created_at": "2026-05-14 09:00",
    },
    {
        "test_name": "Password reset boundary test",
        "module_name": "Authentication",
        "status": "Fail",
        "created_at": "2026-05-14 09:10",
    },
    {
        "test_name": "Dashboard route smoke test",
        "module_name": "Dashboard",
        "status": "Pass",
        "created_at": "2026-05-14 09:20",
    },
]

VALID_STATUSES = {"Pass", "Fail", "Blocked"}

def validate_test_record(test_name, module_name, status):
    test_name = str(test_name).strip()
    module_name = str(module_name).strip()
    status = str(status).strip()

    if not test_name:
        return {"valid": False, "message": "Test name is required."}

    if not module_name:
        return {"valid": False, "message": "Module name is required."}

    if status not in VALID_STATUSES:
        return {"valid": False, "message": "Status must be Pass, Fail, or Blocked."}

    return {"valid": True, "message": "Valid test record."}

def create_test_record(test_name, module_name, status):
    test_name = str(test_name).strip()
    module_name = str(module_name).strip()
    status = str(status).strip()

    validation = validate_test_record(test_name, module_name, status)

    if not validation["valid"]:
        raise ValueError(validation["message"])

    record = {
        "test_name": test_name,
        "module_name": module_name,
        "status": status,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }

    _test_records.append(record)
    return record

def get_all_test_records():
    return list(_test_records)

def calculate_quality_summary(records):
    total = len(records)
    passed = len([record for record in records if record["status"] == "Pass"])
    failed = len([record for record in records if record["status"] == "Fail"])
    blocked = len([record for record in records if record["status"] == "Blocked"])

    pass_rate = 0

    if total > 0:
        pass_rate = round((passed / total) * 100, 2)

    return {
        "total": total,
        "passed": passed,
        "failed": failed,
        "blocked": blocked,
        "pass_rate": pass_rate,
    }

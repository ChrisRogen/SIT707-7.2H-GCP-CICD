from flask import Blueprint, render_template, request, redirect, url_for
from app.services import (
    create_test_record,
    get_all_test_records,
    calculate_quality_summary,
    validate_test_record,
)

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def index():
    summary = calculate_quality_summary(get_all_test_records())
    return render_template("index.html", summary=summary)

@main_bp.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    error = None

    if request.method == "POST":
        test_name = request.form.get("test_name", "").strip()
        module_name = request.form.get("module_name", "").strip()
        status = request.form.get("status", "").strip()

        validation = validate_test_record(test_name, module_name, status)

        if validation["valid"]:
            create_test_record(test_name, module_name, status)
            return redirect(url_for("main.dashboard"))

        error = validation["message"]

    records = get_all_test_records()
    summary = calculate_quality_summary(records)
    return render_template("dashboard.html", records=records, summary=summary, error=error)

@main_bp.route("/health")
def health():
    return {"status": "healthy", "service": "SIT707 Quality Tracker"}, 200

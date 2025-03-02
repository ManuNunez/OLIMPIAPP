from flask import Blueprint, render_template

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/admin_panel')
def admin_panel():
    return render_template('admin/admin_panel.html')
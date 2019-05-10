# app/admin/employee_views.py
from flask import abort, flash, redirect, render_template, url_for
from flask_login import login_required

from . import admin
from .checked_admin import check_admin
from .. import db
from .forms import EmployeeAssignForm, EmployeeForm
from ..models import Employee


@admin.route('/list/employees')
@login_required
def list_employees():
    """
    List all employees
    """
    check_admin()

    employees = Employee.query.all()
    return render_template('admin/employees/employees_list.html',
                           employees=employees, title='Employees')


@admin.route('/assign/employees/<int:id>', methods=['GET', 'POST'])
@login_required
def assign_employee(id):
    """
    Assign a department and a role to an employee
    """
    check_admin()

    employee = Employee.query.get_or_404(id)

    # prevent admin from being assigned a department or role
    if employee.is_admin:
        abort(403)

    form = EmployeeAssignForm(obj=employee)
    if form.validate_on_submit():
        employee.department = form.department.data
        employee.role = form.role.data
        db.session.add(employee)
        db.session.commit()
        flash('You have successfully assigned a department and role.')

        # redirect to the roles page
        return redirect(url_for('admin.list_employees'))

    return render_template('admin/employees/employee.html',
                           employee=employee, form=form,
                           title='Assign Employee')


@admin.route('/add/employee', methods=['GET', 'POST'])
@login_required
def add_employee():
    """
    Add new employee
    """
    check_admin()
    form = EmployeeForm()
    if form.validate_on_submit():
        employee = Employee(email=form.email.data,
                            username=form.username.data,
                            first_name=form.first_name.data,
                            last_name=form.last_name.data,
                            password=form.password.data,
                            department=form.department.data,
                            role=form.role.data)

        # add employee to the database
        db.session.add(employee)
        db.session.commit()
        flash('You have successfully add new employee!')

        # redirect to the login page
        return redirect(url_for('admin.list_employees'))
    # load registration template
    return render_template('admin/employees/employee_add.html', form=form, title='New Employee')

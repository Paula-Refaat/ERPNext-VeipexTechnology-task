
def get_customer_outstanding(customer_name):
    """Return total outstanding amount for the customer."""
    result = frappe.db.sql("""
        SELECT SUM(outstanding_amount)
        FROM `tabSales Invoice`
        WHERE customer = %s AND docstatus = 1
    """, customer_name)
    return result[0][0] or 0.0

outstanding = get_customer_outstanding(doc.name)

if outstanding > 100000:
    doc.custom_risk_level = "High"
elif outstanding > 30000:
    doc.custom_risk_level = "Medium"
else:
    doc.custom_risk_level = "Low"

frappe.msgprint(
    f"Risk Level set to: {doc.custom_risk_level} (Outstanding: {outstanding:,.0f})",
    indicator="blue",
    alert=True
)
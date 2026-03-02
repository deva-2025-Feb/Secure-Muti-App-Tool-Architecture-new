ROLE_PERMISSIONS = {
    "Admin": ["all"],
    "Sales": ["sales_summary", "region_analysis", "model_comparison"],
    "Finance": ["profit_trend", "expense_breakdown"],
    "Operations": ["units_sold_trend"]
}

def check_access(role, tool_name):
    allowed = ROLE_PERMISSIONS.get(role, [])
    return "all" in allowed or tool_name in allowed
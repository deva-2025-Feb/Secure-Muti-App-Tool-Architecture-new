def route_query(query):
    query = query.lower()

    if "revenue" in query and "region" in query:
        return "region_analysis"

    elif "profit" in query:
        return "profit_trend"

    elif "expense" in query:
        return "expense_breakdown"

    elif "units sold" in query:
        return "units_sold_trend"

    elif "sales summary" in query:
        return "sales_summary"

    elif "revenue" in query and "model" in query:
        return "model_comparison"

    else:
        return None
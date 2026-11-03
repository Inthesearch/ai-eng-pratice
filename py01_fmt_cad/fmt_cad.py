def fmt_cad(x):
    if x < 0:
        return f"-${abs(x):,.2f}"
    else:
        return f"${x:,.2f}"

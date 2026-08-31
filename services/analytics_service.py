import pandas as pd

from services.google_sheet import get_sheet_data


def analyze_sales(question: str, sheet_url: str):

    data = get_sheet_data(sheet_url)

    df = pd.DataFrame(data)

    total_sales = df["amount"].sum()

    highest_sale = df.loc[df["amount"].idxmax()]

    product_sales = (
        df.groupby("product")["amount"]
        .sum()
        .sort_values(ascending=False)
    )

    return {
        "question": question,
        "total_sales": float(total_sales),
        "highest_transaction": highest_sale.to_dict(),
        "sales_by_product": product_sales.to_dict(),
    }
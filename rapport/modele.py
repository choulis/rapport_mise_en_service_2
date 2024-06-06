

from pandas import DataFrame


def generer_html(**infos):
    return f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Document</title>
            </head>
            <body>
                <h1>{infos['title'].upper()}</h1>
                <h2>Compresseurs</h2>
                {infos['tableau'].to_html()}
            </body>
            </html>
        """
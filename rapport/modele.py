

def generer_html(tableau):
    return f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Document</title>
            </head>
            <body>
                <h1>Rapport de mise en service</h1>
                <h2>Compresseurs</h2>
                {tableau.to_html()}
            </body>
            </html>
        """
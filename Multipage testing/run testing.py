import dash
from dash import html, dcc
#import dash_bootstrap_components as dbc
from dash_labs.plugins.pages import register_page

app = dash.Dash(__name__,use_pages=True)


app.layout = html.Div([
	html.H1('Multi-page app with Dash Pages'),

    html.Div(
        [
            html.Div(
                dcc.Link(
                    f"{page['name']} - {page['path']}", href=page["path"]
                )
            )
            for page in dash.page_registry.values()
        ]
    ),

	dash.page_container
])

if __name__ == '__main__':
    app.run(host = '127.0.0.1',port = 8085,debug = True)
  
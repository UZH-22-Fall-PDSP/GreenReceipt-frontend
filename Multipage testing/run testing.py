import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
# dbc = ash_bootstrap_components



app = dash.Dash(__name__,use_pages=True)

# app.layout = html.Div([
#     dcc.Location(id="url"),
#     navigation,
#     dash.page_container
# ])

app.layout = html.Div(
    [
        # main app framework
        # html.Div("Green Recipe", style={'fontSize':50, 'textAlign':'center'}),
        html.Div([
            dcc.Link(page['name']+"  |  ", href=page['path'])
            for page in dash.page_registry.values()
        ]),
        html.Hr(),
        # dcc.Location(id='url'),

        # html.Div(id='page-content'),
        # content of each page
        dash.page_container
    ]
)

# @app.callback([Output("page-content", "children"),
#               Input('url', 'pathname')
#               ])

# def display_content(pathname):

#     if pathname == '/':
#         return home.layout

#     elif pathname == '/a':
#         return archive.layout()
        
#     else:
#         return home.layout
if __name__ == '__main__':
    app.run(host = '127.0.0.1',port = 8085,debug = True)

     
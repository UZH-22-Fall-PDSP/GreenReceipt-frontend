import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash_labs.plugins.pages import register_page

app = dash.Dash(__name__,use_pages=True)


# app.layout = html.Div([
# 	html.H1('Multi-page app with Dash Pages'),

#     html.Div(
#         [
#             html.Div(
#                 dcc.Link(
#                     f"{page['name']}", href=page['path']
#                 )
#             )
#             for page in dash.page_registry.values()
#         ]
#     ),

# 	dash.page_container
# ])

app.layout = html.Div([

    html.Div(
        [
            html.Div(
                dcc.Link(
                    f"{page['name']}", href=page['path']
                )
            )
            for page in dash.page_registry.values()
            
        ]
    ),

	dash.page_container
])

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
    app.run_server(host = '127.0.0.1',port = 8085,debug = True)

print(dash.page_registry.values())    
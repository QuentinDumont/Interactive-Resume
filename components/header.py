import dash_html_components as html
import dash_core_components as dcc

def Header():
    return html.Div([
        get_logo(),
        get_header(),
        html.Br([]),
        get_menu()
    ])

def get_logo():
    logo = html.Div([

        html.Div([
            html.Img(src='https://i.ibb.co/2W4WKC2/upload.jpg', height='100', width='110')
        ], className="ten columns padded", style = dict(width = '123px', height = '123px')),

        html.Div([
            html.P('JUNIOR DATA ANALYST')], style = {'font-size': '40px',
            'color': 'rgb(198, 0, 0)',
            'margin-bottom': '0px',
            'font-weight': 'bold',
            'padding-top': '0px'}),

        html.Div([
            html.P('HARVEY NASH')], style = {'font-size': '40px',
            'color': 'black',
            'margin-left': '300px',
            'font-weight': 'bold',
            'padding-top': '0px'}),

        html.Div([
            dcc.Link('Full View   ', href='/quentin-dumont/full-view')
        ], className="two columns page-view no-print", style = {'text-align': 'right', 'padding-bottom': '10px', 'padding-top': '0px', 'width' : '95%'})

    ], className="row gs-header")
    return logo


def get_header():
    header = html.Div([

        html.Div([
            html.H5(
                'Quentin DUMONT - Interactive Resume')
        ], className="twelve columns padded")

    ], className="row gs-header gs-text-header")
    return header


def get_menu():
    menu = html.Div([

        dcc.Link('Overview   ', href='/quentin-dumont/overview', className="tab first"),

        dcc.Link('Professional Experiences   ', href='/quentin-dumont/professional-experience', className="tab"),

        dcc.Link('Skills   ', href='/quentin-dumont/skills', className="tab"),

        dcc.Link("Next steps ?   ", href='/quentin-dumont/what-is-next', className="tab")

    ], className="row ", style = {'text-align': 'center', 'font-weight' : 'bold'})
    return menu

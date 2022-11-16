from flask import current_app as app
from flask_assets import Bundle

def compile_assets(assets):
    assets.auto_build = True
    assets.debug = False
    
    main_style_bundle = Bundle(
        'src/less/*.less',
        'home_bp/homepage.less',
        filters='less,cssmin',
        output='dist/css/style.min.css',
        extra={'rel': 'stylesheet/css'}
    )

    main_js_bundle = Bundle(
        'src/js/main.js',
        filters='jsmin',
        output='dist/js/main.min.js'
    )

    assets.register('main_style_bundle', main_style_bundle)
    assets.register('main_js_bundle', main_js_bundle)
    # Build bundles
    main_style_bundle.build()
    main_js_bundle.build()
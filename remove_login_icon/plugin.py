from ckan.plugins import SingletonPlugin, implements, IConfigurer

class RemoveLoginIconPlugin(SingletonPlugin):
    implements(IConfigurer)

    def update_config(self, config):
        # Add custom CSS to remove the login icon
        config['extra_public_paths'] = ','.join([
            config.get('extra_public_paths', ''),
            'ckanext/remove_login_icon/public',
        ])
        config['extra_template_paths'] = ','.join([
            config.get('extra_template_paths', ''),
            'ckanext/remove_login_icon/templates',
        ])

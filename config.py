import os

class  Config:
    def __init__(self, scriptname):
        self.scriptname = scriptname

        self.folders = ['app', 'tests', 'requirements',
                  'app\\auth', 'app\\main', 'app\\static', 'app\\templates', 'app\\api',
                  ]

        self.files = ['config.py', f'{self.scriptname}',
                'app\\__init__.py', 'app\\models.py', 'app\\decorators.py',
                'app\\static\\styles.css',
                'app\\templates\\base.html',
                'app\\main\\__init__.py', 'app\\main\\errors.py', 'app\\main\\forms.py', 'app\\main\\views.py',
                'app\\auth\\__init__.py', 'app\\auth\\forms.py', 'app\\auth\\views.py',
                'tests\\__init__.py', 'tests\\test_basics.py',
                'requirements\\common.txt', 'requirements\\dev.txt', 'requirements\\prod.txt',
                'app\\api\\__init__.py', 'app\\api\\users.py', 'app\\api\\posts.py', 'app\\api\\comments.py', 'app\\api\\authentication.py', 'app\\api\\errors.py', 'app\\api\\decorators.py',]
    
    @property
    def scriptname(self):
        return self._scriptname

    @scriptname.setter
    def scriptname(self, value):
        if str(value).endswith('.py'):
            self._scriptname = value
        else:
            self._scriptname = f'{value}.py'
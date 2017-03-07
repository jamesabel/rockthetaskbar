
import osnap.installer

import rockthetaskbar


def make_installer():
    osnap.installer.make_installer(rockthetaskbar.__python_version__, rockthetaskbar.__application_name__,
                                   rockthetaskbar.__author__, 'hello world for a taskbar app',
                                   'https://github.com/jamesabel/rockthetaskbar')


if __name__ == '__main__':
    make_installer()

project('pymt_heatf', 'fortran', 'cython')

py = import('python').find_installation(pure: false)
fc = meson.get_compiler('fortran')

python_inc = py.get_path('data') / 'include'
numpy_inc = run_command(
    py,
    [
        '-c',
        'import numpy; print(numpy.get_include())'
    ],
    check: true
).stdout().strip()
incs = include_directories(
    [
        'pymt_heatf/lib',
        python_inc,
        numpy_inc,
    ]
)

deps = [
    # fc.find_library('bmif'),
    # fc.find_library('heatf'),
    # fc.find_library('bmiheatf'),
    dependency('bmif', method: 'pkg-config'),
    dependency('heatf', method: 'pkg-config'),
    dependency('bmiheatf', method: 'pkg-config'),
]

srcs = [
    'pymt_heatf/lib/bmi_interoperability.f90',
    'pymt_heatf/lib/heatmodelf.pyx',
]

# Files get copied to <python directory>/site-packages/<subdir>
install_pkg_srcs = [
    'pymt_heatf/__init__.py',
    'pymt_heatf/bmi.py',
]
py.install_sources(
    install_pkg_srcs,
    subdir: 'pymt_heatf',
)
install_lib_srcs = [
    'pymt_heatf/lib/__init__.py',
    'pymt_heatf/lib/heatmodelf.pyx',
]
py.install_sources(
    install_lib_srcs,
    subdir: 'pymt_heatf/lib',
)

install_subdir(
    'meta/HeatModelF',
    install_dir: py.get_install_dir() / 'pymt_heatf/data',
)

py.extension_module(
    'heatmodelf',
    srcs,
    dependencies: deps,
    include_directories: incs,
    install: true,
    subdir: 'pymt_heatf/lib',
)

# This is a temporary fix for editable installs.
run_command('cp', '-r', 'pymt_heatf/data', 'build')

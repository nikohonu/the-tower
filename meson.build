project(
        'the-tower',
        'cpp',
        'c',
        default_options: ['cpp_std=c++26'],
        license: 'MIT',
)

sdl2_dep = dependency('sdl2')

globber = run_command('sh', '-c', 'find src -name "*.cpp" | sort', check: true)
src = globber.stdout().strip().split('\n')

executable('the-tower', src, dependencies: sdl2_dep)

{
  'includes': ['../../build/common.gypi'],
  'targets': [
    {
      'target_name': 'v8_ken_shell',
      'type': 'executable',
      'dependencies': [
        'v8.gyp:v8',
        'ken',
      ],
      'include_dirs': [
        '../../include',
      ],
      'sources': [
        '../../src/v8-ken-main.cc',
      ],
    },
    {
      'target_name': 'ken',
      'type': '<(library)',
      'cflags!': [
        '-Wnon-virtual-dtor',
        '-Woverloaded-virtual',
        '-Werror',
        '-fno-rtti',
      ],
      'cflags': [
        '-std=gnu99',
      ],
      'include_dirs': [
        '../../deps/ken',
      ],
      'sources': [
        '../../deps/ken/ken.c',
        '../../deps/ken/kencom.c',
        '../../deps/ken/kencrc.c',
        '../../deps/ken/kenext.c',
        '../../deps/ken/kenpat.c',
        '../../deps/ken/kenvar.c',
      ],
    },
  ]
}

{
  "targets": [
    {
      "includes": [
        "auto.gypi"
      ],
      "sources": [
        "src/run.cpp"
      ],
      #'cflags!': [ '-m32', '-fno-omit-frame-pointer', '-pthread', '-Wall', '-Wextra', '-Wno-unused-parameter' ],
      #'cflags_cc!': [ '-fno-rtti', '-fno-exceptions', '-std=gnu++0x' ],
      #'ldflags!': [ '-pthread', '-rdynamic' ],
      "cflags_cc": [
        "-pipe",
        "-Wall",
        "-O3",
        "-fomit-frame-pointer",
        "-march=native",
        "-fopenmp",
        "-D_FILE_OFFSET_BITS=64",
        "-I/usr/include/apr-1"
      ],
      "link_settings":{
        "ldflags": [
          "-L<(module_root_dir)/src -lbinarytrees",
          "-Wl,-rpath=<(module_root_dir)/src",
          #"-Wl,-z,defs",
          "-lapr-1 -lgomp -lm"
        ]
      }
    }
  ],
  "includes": [
    "auto-top.gypi"
  ]
}

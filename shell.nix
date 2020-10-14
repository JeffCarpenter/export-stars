let
  pkgs = import <nixpkgs> { };

  customPython = pkgs.python38.buildEnv.override {
    extraLibs = [ pkgs.python38Packages.PyGithub ];
  };
in pkgs.mkShell { buildInputs = [ customPython ]; }

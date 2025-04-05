#! /bin/bash
pygmentize -O style=kappa_style_browser     -o img/kappa_edit_notation_style_browser.png    example_files/kappa_comprehensive.ka
pygmentize -O style=kappa_style_demo        -o img/kappa_edit_notation_style_demo.png       example_files/kappa_comprehensive.ka
pygmentize -O style=kappa_style_edit_dark   -o img/kappa_edit_notation_style_edit_dark.png  example_files/kappa_comprehensive.ka
pygmentize -O style=kappa_style_edit        -o img/kappa_edit_notation_style_edit.png       example_files/kappa_comprehensive.ka
pygmentize -O style=katie_style_deltas      -o img/katie_style_deltas.png                   example_files/katie_big_wnt_query.katie
pygmentize -O style=katie_style_deltas_dark -o img/katie_style_deltas_dark.png              example_files/katie_big_wnt_query.katie

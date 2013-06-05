{
  'includes': [ '../../common.gyp' ],
  'targets': [
    {
      'target_name': 'liblept',
      'type': 'static_library',
      'include_dirs': [
        'src',
      ],
      'sources': [
        'src/adaptmap.c',
        'src/affine.c',
        'src/affinecompose.c',
        'src/arithlow.c',
        'src/arrayaccess.c',
        'src/bardecode.c',
        'src/baseline.c',
        'src/bbuffer.c',
        'src/bilinear.c',
        'src/binarize.c',
        'src/binexpand.c',
        'src/binexpandlow.c',
        'src/binreduce.c',
        'src/binreducelow.c',
        'src/blend.c',
        'src/bmf.c',
        'src/bmpio.c',
        'src/bmpiostub.c',
        'src/boxbasic.c',
        'src/boxfunc1.c',
        'src/boxfunc2.c',
        'src/boxfunc3.c',
        'src/boxfunc4.c',
        'src/bytearray.c',
        'src/ccbord.c',
        'src/ccthin.c',
        'src/classapp.c',
        'src/colorcontent.c',
        'src/coloring.c',
        'src/colormap.c',
        'src/colormorph.c',
        'src/colorquant1.c',
        'src/colorquant2.c',
        'src/colorseg.c',
        'src/colorspace.c',
        'src/compare.c',
        'src/conncomp.c',
        'src/convertfiles.c',
        'src/convolve.c',
        'src/convolvelow.c',
        'src/correlscore.c',
        'src/dewarp.c',
        'src/dnabasic.c',
        'src/dwacomb.2.c',
        'src/dwacomblow.2.c',
        'src/edge.c',
        'src/enhance.c',
        'src/fhmtauto.c',
        'src/fhmtgen.1.c',
        'src/fhmtgenlow.1.c',
        'src/finditalic.c',
        'src/flipdetect.c',
        'src/fliphmtgen.c',
        'src/fmorphauto.c',
        'src/fmorphgen.1.c',
        'src/fmorphgenlow.1.c',
        'src/fpix1.c',
        'src/fpix2.c',
        # Compile without freetype.
        #'src/freetype.c',
        'src/gifio.c',
        'src/gifiostub.c',
        'src/gplot.c',
        'src/graphics.c',
        'src/graymorph.c',
        'src/graymorphlow.c',
        'src/grayquant.c',
        'src/grayquantlow.c',
        'src/heap.c',
        'src/jbclass.c',
        'src/jpegio.c',
        'src/jpegiostub.c',
        'src/kernel.c',
        'src/leptwin.c',
        'src/libversions.c',
        'src/list.c',
        'src/maze.c',
        'src/morph.c',
        'src/morphapp.c',
        'src/morphdwa.c',
        'src/morphseq.c',
        'src/numabasic.c',
        'src/numafunc1.c',
        'src/numafunc2.c',
        'src/pageseg.c',
        'src/paintcmap.c',
        'src/parseprotos.c',
        'src/partition.c',
        'src/pdfio.c',
        'src/pdfiostub.c',
        'src/pix1.c',
        'src/pix2.c',
        'src/pix3.c',
        'src/pix4.c',
        'src/pix5.c',
        'src/pixabasic.c',
        'src/pixacc.c',
        'src/pixafunc1.c',
        'src/pixafunc2.c',
        'src/pixalloc.c',
        'src/pixarith.c',
        'src/pixcomp.c',
        'src/pixconv.c',
        'src/pixtiling.c',
        'src/pngio.c',
        'src/pngiostub.c',
        'src/pnmio.c',
        'src/pnmiostub.c',
        'src/projective.c',
        'src/psio1.c',
        'src/psio1stub.c',
        'src/psio2.c',
        'src/psio2stub.c',
        'src/ptabasic.c',
        'src/ptafunc1.c',
        'src/ptra.c',
        'src/quadtree.c',
        'src/queue.c',
        'src/rank.c',
        'src/readbarcode.c',
        'src/readfile.c',
        'src/regutils.c',
        'src/rop.c',
        'src/ropiplow.c',
        'src/roplow.c',
        'src/rotate.c',
        'src/rotateam.c',
        'src/rotateamlow.c',
        'src/rotateorth.c',
        'src/rotateorthlow.c',
        'src/rotateshear.c',
        'src/runlength.c',
        'src/sarray.c',
        'src/scale.c',
        'src/scalelow.c',
        'src/seedfill.c',
        'src/seedfilllow.c',
        'src/sel1.c',
        'src/sel2.c',
        'src/selgen.c',
        'src/shear.c',
        'src/skew.c',
        'src/spixio.c',
        'src/stack.c',
        'src/sudoku.c',
        'src/textops.c',
        'src/tiffio.c',
        'src/tiffiostub.c',
        'src/utils.c',
        'src/viewfiles.c',
        'src/warper.c',
        'src/watershed.c',
        'src/webpio.c',
        'src/webpiostub.c',
        'src/writefile.c',
        'src/zlibmem.c',
        'src/zlibmemstub.c',
      ],
    },
  ]
}

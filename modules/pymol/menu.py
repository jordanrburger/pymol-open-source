#A* -------------------------------------------------------------------
#B* This file contains source code for the PyMOL computer program
#C* copyright 1998-2000 by Warren Lyford Delano of DeLano Scientific. 
#D* -------------------------------------------------------------------
#E* It is unlawful to modify or remove this copyright notice.
#F* -------------------------------------------------------------------
#G* Please see the accompanying LICENSE file for further information. 
#H* -------------------------------------------------------------------
#I* Additional authors of this source file include:
#-* 
#-* 
#-*
#Z* -------------------------------------------------------------------

# pmm.py 
# This section contains the menu contents and the associated commands
#

def mol_show(s):
   return [[ 2, 'Show:'      , ''                               ],
           [ 1, 'lines'      , 'cmd.show("lines"     ,"'+s+'")' ],
           [ 1, 'nonbonded'  , 'cmd.show("nonbonded" ,"'+s+'")' ],
           [ 1, 'sticks'     , 'cmd.show("sticks"    ,"'+s+'")' ],
           [ 1, 'ribbon'     , 'cmd.show("ribbon"    ,"'+s+'")' ],
           [ 1, 'cartoon'    , 'cmd.show("cartoon"   ,"'+s+'")' ],
           [ 0, ''           , ''                               ],
           [ 1, 'labels'     , 'cmd.show("labels"    ,"'+s+'")' ],
           [ 1, 'cell'       , 'cmd.show("cell"      ,"'+s+'")' ],
           [ 0, ''           , ''                               ],
           [ 1, 'dots'       , 'cmd.show("dots"      ,"'+s+'")' ],
           [ 1, 'spheres'    , 'cmd.show("spheres"   ,"'+s+'")' ],
           [ 1, 'nb_spheres' , 'cmd.show("nb_spheres","'+s+'")' ],
           [ 0, ''           , ''                               ],
           [ 1, 'mesh'       , 'cmd.show("mesh"      ,"'+s+'")' ],
           [ 1, 'surface'    , 'cmd.show("surface"   ,"'+s+'")' ],
           ]

def mol_hide(s):
   return [[ 2, 'Hide:'     , ''                                ],
           [ 1, 'lines'     , 'cmd.hide("lines"     ,"'+s+'")'  ],
           [ 1, 'nonbonded' , 'cmd.hide("nonbonded" ,"'+s+'")'  ],           
           [ 1, 'sticks'    , 'cmd.hide("sticks"    ,"'+s+'")'  ],
           [ 1, 'ribbon'    , 'cmd.hide("ribbon"    ,"'+s+'")'  ],
           [ 1, 'cartoon'   , 'cmd.hide("cartoon"   ,"'+s+'")' ],           
           [ 0, ''          , ''                                ],
           [ 1, 'labels'    , 'cmd.hide("labels"    ,"'+s+'")'  ],
           [ 1, 'cell'      , 'cmd.hide("cell"      ,"'+s+'")' ],
           [ 0, ''          , ''                                ],
           [ 1, 'dots'      , 'cmd.hide("dots"      ,"'+s+'")'  ],
           [ 1, 'spheres'   , 'cmd.hide("spheres"   ,"'+s+'")'  ],
           [ 1, 'nb_spheres', 'cmd.hide("nb_spheres","'+s+'")'  ],           
           [ 0, ''          , ''                                ],
           [ 1, 'mesh'      , 'cmd.hide("mesh"      ,"'+s+'")'  ],
           [ 1, 'surface'   , 'cmd.hide("surface"   ,"'+s+'")'  ],
           [ 0, ''          , ''                                ],
           [ 1, 'hydrogens' , 'cmd.hide("('+s+' and hydro)")'   ],
           [ 1, 'everything', 'cmd.hide("('+s+')")'             ],
           [ 0, ''          , ''                                ],           
           [ 1, 'unselected', 'cmd.hide("(not '+s+')")'         ],
           ]

def dist_show(s):
   return [[ 2, 'Show:'     , ''                               ],
           [ 1, 'dashes'    , 'cmd.show("dashes"    ,"'+s+'")' ],
           [ 1, 'labels'    , 'cmd.show("labels"    ,"'+s+'")' ]
          ]   

def dist_hide(s):
   return [[ 2, 'Hide:'     , ''                                ],
           [ 1, 'dashes'    , 'cmd.hide("dashes"    ,"'+s+'")'  ],
           [ 1, 'labels'    , 'cmd.hide("labels"    ,"'+s+'")'  ]
          ]

def simple_show(s):
   return [[ 2, 'Show:'       , ''                             ],
           [ 1, 'everything'  , 'cmd.enable("'+s+'")'          ]]

def simple_hide(s):
   return [[ 2, 'Hide:'     ,''                                ],
           [ 1, 'everything'    ,'cmd.disable("'+s+'")'        ]]

def mesh_show(s):
   return [[ 2, 'Show:'       , ''                             ],
           [ 1, 'cell'        , 'cmd.show("cell","'+s+'")'     ],
           [ 1, 'everything'  , 'cmd.enable("'+s+'")'          ]]

def mesh_hide(s):
   return [[ 2, 'Hide:'       , ''                             ],
           [ 1, 'cell'        , 'cmd.hide("cell","'+s+'")'      ],           
           [ 1, 'everything'  , 'cmd.disable("'+s+'")'          ]]

def mol_color(s):
   return [[ 2, 'Color:'     ,''                               ],
           [ 1, '`292C`777H`229N`922O`950S`905*'  , 'util.cbag("'+s+'")'],
           [ 1, '`099C`777H`229N`922O`950S`905*'  , 'util.cbac("'+s+'")'],
           [ 1, '`990C`777H`229N`922O`950S`905*'  , 'util.cbay("'+s+'")'],
           [ 1, '`955C`777H`229N`922O`950S`905*'  , 'util.cbas("'+s+'")'],
           [ 1, '`777C`777H`229N`922O`950S`905*'  , 'util.cbaw("'+s+'")'],
           [ 1, '`559C`777H`229N`922O`950S`905*'  , 'util.cbab("'+s+'")'],
           [ 0, ''                                , ''                 ],
           [ 1, '`900r`950a`990i`090n`099b`059o`009w', 'util.rainbow("'+s+'")'],
           [ 1, '`900r`950a`990i`090n`099b`059o`009w`999(*/ca)', 'util.rainbow("('+s+')&*/ca")'],                      
           [ 0, ''                                , ''                 ],           
           [ 1, '`900red'         , 'cmd.color("red","'+s+'")'     ],
           [ 1, '`090green'       , 'cmd.color("green","'+s+'")'   ],
           [ 1, '`009blue'        , 'cmd.color("blue","'+s+'")'    ],
           [ 1, '`990yellow'      , 'cmd.color("yellow","'+s+'")'  ],
           [ 1, '`909violet'      , 'cmd.color("violet","'+s+'")'  ],
           [ 1, '`099cyan'        , 'cmd.color("cyan","'+s+'")'    ],           
           [ 1, '`955salmon'      , 'cmd.color("salmon","'+s+'")'  ],
           [ 1, '`595lime'        , 'cmd.color("lime","'+s+'")'    ],
           [ 1, '`968pink'  ,'cmd.color("pink","'+s+'")'  ],
           [ 1, '`559slate'       , 'cmd.color("slate","'+s+'")'   ],
           [ 1, '`905magenta'     , 'cmd.color("magenta","'+s+'")' ],
           [ 1, '`950orange'      , 'cmd.color("orange","'+s+'")'  ],
           [ 1, '`059marine'      , 'cmd.color("marine","'+s+'")'  ],
           [ 1, '`551olive'       , 'cmd.color("olive","'+s+'")'   ],
           [ 1, '`626purple'      , 'cmd.color("purple","'+s+'")'  ],
           [ 1, '`266teal'        , 'cmd.color("teal","'+s+'")'    ],
           [ 1, '`151forest'      , 'cmd.color("forest","'+s+'")'  ],
           [ 1, '`611firebrick'   , 'cmd.color("firebrick","'+s+'")'  ],
           [ 1, '`631chocolate'   , 'cmd.color("chocolate","'+s+'")'  ],           
           [ 1, '`999white'       , 'cmd.color("white","'+s+'")'   ],
           [ 1, '`987wheat'       , 'cmd.color("wheat","'+s+'")'   ],
           [ 1, '`555grey'        , 'cmd.color("grey","'+s+'")'    ]
           ]

def general_color(s):
   return [[ 2, 'Color:'     ,''                        ],
           [ 1, '`900red'         ,'cmd.color("red","'+s+'")'  ],
           [ 1, '`090green'       ,'cmd.color("green","'+s+'")'  ],
           [ 1, '`009blue'        ,'cmd.color("blue","'+s+'")'  ],
           [ 1, '`990yellow'      ,'cmd.color("yellow","'+s+'")'  ],
           [ 1, '`909violet'  ,'cmd.color("violet","'+s+'")'  ],
           [ 1, '`099cyan'  ,'cmd.color("cyan","'+s+'")'  ],           
           [ 1, '`955salmon'      ,'cmd.color("salmon","'+s+'")'  ],
           [ 1, '`595lime' ,'cmd.color("lime","'+s+'")'  ],
           [ 1, '`967pink'  ,'cmd.color("pink","'+s+'")'  ],
           [ 1, '`559slate'  ,'cmd.color("slate","'+s+'")'  ],
           [ 1, '`905magenta' ,'cmd.color("magenta","'+s+'")'  ],
           [ 1, '`950orange'      ,'cmd.color("orange","'+s+'")'  ],
           [ 1, '`059marine'      ,'cmd.color("marine","'+s+'")'  ],
           [ 1, '`551olive'   ,'cmd.color("olive","'+s+'")'  ],
           [ 1, '`626purple'  ,'cmd.color("purple","'+s+'")'  ],
           [ 1, '`266teal'  ,'cmd.color("teal","'+s+'")'  ],
           [ 1, '`151forest'  ,'cmd.color("forest","'+s+'")'  ],
           [ 1, '`611firebrick'   , 'cmd.color("firebrick","'+s+'")'  ],
           [ 1, '`631chocolate'   , 'cmd.color("chocolate","'+s+'")'  ],           
           [ 1, '`999white'       ,'cmd.color("white","'+s+'")'  ],
           [ 1, '`987wheat'       , 'cmd.color("wheat","'+s+'")'   ],
           [ 1, '`555grey'    ,'cmd.color("grey","'+s+'")'  ]
           ]

def sele_action(s):
   return [[ 2, 'Actions:'     ,''                        ],     
           [ 1, 'origin'   ,'cmd.origin("'+s+'")'         ],
           [ 1, 'zoom'         ,'cmd.zoom("'+s+'")'       ],
           [ 1, 'orient'       ,'cmd.orient("'+s+'")'     ],
           [ 0, ''          ,''                           ],
           [ 1, 'delete'       ,'cmd.delete("'+s+'")'     ],
           [ 0, ''          ,''                           ],
           [ 1, 'residues' ,'cmd.select("'+s+'","(byres '+s+')",show=1)'      ],
           [ 0, ''          ,''                                              ],
           [ 1, 'expand by 4 A'  ,'cmd.select("'+s+'","('+s+' expand 4)",show=1)' ],
           [ 1, 'expand by 8 A'  ,'cmd.select("'+s+'","('+s+' expand 8)",show=1)' ],
           [ 0, ''          ,''                                              ],
           [ 1, 'invert'  ,'cmd.select("'+s+'","(not '+s+')",show=1)'        ],
           [ 0, ''          ,''                                              ],
           [ 1, 'create object'       ,'cmd.create(None,"'+s+'")'     ],           
           [ 1, 'remove atoms'  ,'cmd.remove("'+s+'")'        ],
           [ 0, ''          ,''                                              ],
           [ 1, 'mask'  ,'cmd.mask("'+s+'")'        ],
           [ 1, 'unmask'  ,'cmd.unmask("'+s+'")'        ],
           [ 0, ''          ,''                                              ],
           [ 1, 'protect'  ,'cmd.protect("'+s+'")'        ],
           [ 1, 'deprotect'  ,'cmd.deprotect("'+s+'")'        ],
           [ 0, ''          ,''                                              ],
           [ 1, 'count atoms'  ,'cmd.count_atoms("'+s+'")'        ],           
           [ 0, ''          ,''                                              ],
           [ 1, 'duplicate'           ,'cmd.select("'+s+'")'     ],
           ]

def mol_action(s):
   return [[ 2, 'Actions:'     , ''                       ],     
           [ 1, 'origin'       , 'cmd.origin("'+s+'")'    ],
           [ 1, 'zoom'         , 'cmd.zoom("'+s+'")'      ],
           [ 1, 'orient'       , 'cmd.orient("'+s+'")'    ],
           [ 0, ''             , ''                       ],
           [ 1, 'delete'       , 'cmd.delete("'+s+'")'    ],
           [ 0, ''          ,''                                              ],
           [ 1, 'mask'  ,'cmd.mask("'+s+'")'        ],
           [ 1, 'unmask'  ,'cmd.unmask("'+s+'")'        ],
           [ 0, ''          ,''                                              ],
           [ 1, 'protect'  ,'cmd.protect("'+s+'")'        ],
           [ 1, 'deprotect'  ,'cmd.deprotect("'+s+'")'        ],
           [ 0, ''          ,''                                              ],
           [ 1, 'assign S.S.'  ,'util.ss("'+s+'")'        ],
           [ 0, ''          ,''                                              ],
           [ 1, 'count atoms'  ,'cmd.count_atoms("'+s+'")'        ],
           [ 0, ''          ,''                                              ],           
           [ 1, 'duplicate'       ,'cmd.create(None,"'+s+'")'     ],           
           ]

def simple_action(s):
   return [[ 2, 'Actions:'     , ''                       ],
           [ 1, 'origin'       , 'cmd.origin("'+s+'")'    ],
           [ 1, 'zoom'         , 'cmd.zoom("'+s+'")'      ],
           [ 0, ''             , ''                       ],
           [ 1, 'delete'       , 'cmd.delete("'+s+'")'    ],
           ]

def all_action(s):
   return [[ 2, 'Actions:'     , ''                      ],     
           [ 1, 'origin'   , 'cmd.origin("'+s+'")'   ],
           [ 1, 'zoom'         , 'cmd.zoom("'+s+'")'     ],
           [ 0, ''             , ''                      ],
           [ 1, 'delete'       , 'cmd.delete("all")'     ]
           ]


def mol_labels(s):
   return [[ 2, 'Labels:'        , ''                                  ],
           [ 1, 'clear'          , 'cmd.label("'+s+'","\'\'")'         ],
           [ 1, 'residues'       ,
  'cmd.label("(name ca and (byres('+s+')))","\'%s-%s\'%(resn,resi)")'  ],
           [ 1, 'atoms'          , 'cmd.label("'+s+'","name")'         ],
           [ 0, ''               , ''                                  ],
           [ 1, 'b-factor'       , 'cmd.label("'+s+'","\'%1.2f\'%b")'  ],           [ 1, 'Partial Charge' , 
  'cmd.label("'+s+'","\'%1.4f\'%partial_charge")'                      ],
           [ 1, 'formal charge' , 
  'cmd.label("'+s+'","\'%d\'%formal_charge")'                      ],
           [ 0, ''               , ''                                  ],
           [ 1, 'text type'      , 'cmd.label("'+s+'","text_type")'    ],
           [ 1, 'numeric Type'   , 'cmd.label("'+s+'","numeric_type")' ],
           [ 0, ''               , ''                                  ],      
           [ 1, 'ID'             , 'cmd.label("'+s+'","id")' ],
           [ 1, 'ID+1'           , 'cmd.label("'+s+'","id+1")' ],
           ]


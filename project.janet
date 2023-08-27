(declare-project
  :name "glyph"
  :description "A roguelike game"

  :dependencies ["https://github.com/Alligator/jtermbox.git"])


(declare-executable
  :name "glyph"
  :entry "src/glyph.janet"
  :install true)

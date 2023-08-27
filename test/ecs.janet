(import ../src/lib/ecs)

(assert (deep= (ecs/add-entity @{}) @{:id 0}))
(assert (deep= (ecs/add-entity @{:hello "world"}) @{:id 1 :hello "world"}))

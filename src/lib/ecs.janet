(def- entities (array/new 1000))

(defn add-entity [entity]
  (put entity :id (length entities))
  (array/push entities entity)
  entity)

(defn remove-entity [entity]
  (put entities (entity :id) nil))

(defn get-entity [id]
  (entities id))

(defn get-entities-with [& components]
  (filter (fn [entity]
            (all (fn [component]
                   (truthy? (entity component)))
                 components))
          entities))

(defn set-entity [entity]
  (put entities (entity :id) entity))

(def- systems (array/new 100))

(defn add-system [system]
  (array/push systems system)
  system)

(defn tick []
  (each systems (fn [system]
                  (system entities)))

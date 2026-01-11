# Object Pool Manager


class Object:
    def __init__(self, id: int):
        self.id = id

    def reset_object(self):
        # reset objects other fields
        pass

    def __str__(self):
        return f"Obj Id = {self.id}"


class ObjectPoolManager:
    def __init__(self, number_of_objects: int):
        self.number_of_objects = number_of_objects
        self.available_objects = []
        self.acquired_objects = []

        for i in range(number_of_objects):
            self.available_objects.append(Object(i))

    def acquire_object(self):
        if len(self.available_objects):
            obj = self.available_objects.pop()
            self.acquired_objects.append(obj)
            return obj
        else:
            print("No objects available in pool")

    def release_object(self, obj: Object):
        obj.reset_object()
        self.acquired_objects.remove(obj)
        self.available_objects.append(obj)


if __name__ == "__main__":
    pool = ObjectPoolManager(5)

    obj1 = pool.acquire_object()
    print(obj1)
    obj2 = pool.acquire_object()
    print(obj2)
    obj3 = pool.acquire_object()
    print(obj3)
    obj4 = pool.acquire_object()
    print(obj4)
    obj5 = pool.acquire_object()
    print(obj5)

    print(f"{len(pool.acquired_objects) = } and {len(pool.available_objects) = }")
    #   obj6 = pool.acquire_object() # No object available in pool
    pool.release_object(obj5)
    print(f"{len(pool.acquired_objects) = } and {len(pool.available_objects) = }")

    pool.release_object(obj4)
    print(f"{len(pool.acquired_objects) = } and {len(pool.available_objects) = }")

    pool.release_object(obj3)
    print(f"{len(pool.acquired_objects) = } and {len(pool.available_objects) = }")

    pool.release_object(obj2)
    print(f"{len(pool.acquired_objects) = } and {len(pool.available_objects) = }")

    pool.release_object(obj1)
    print(f"{len(pool.acquired_objects) = } and {len(pool.available_objects) = }")

from elements.containers import DEFAULT_OUTPUT_FILE, DEFAULT_GROUP_NAME, DEFAULT_INPUT_FILE
import inspect
import pickle


class Group:

    name = DEFAULT_GROUP_NAME

    def __init__(self):
        self.elems = []

    def set_name(self, name=None):
        self.name = name if name else input('Enter a name of Group: ')

    def add_by_class(self, other):
        if inspect.isclass(other):
            self.elems.append(other().set())
        else:
            print ('WARNING! CANNOT ADD {}\nITS NOT A CLASS\n'.format(other))

    def show(self):
        list(map(lambda el: el.show() if hasattr(el, 'show') else None, self.elems))

    def to_file(self, file_name=DEFAULT_OUTPUT_FILE):
        with open(file_name, 'wb') as f:
            pickle.dump(self.elems, f)
            print ('{} successfully created'.format(file_name))

    def read_file(self, file_name=None):
        file_name = file_name if file_name else raw_input('Enter file name: ')
        with open(file_name, 'wb') as f:
            self.elems = pickle.load(f)

    def clean(self):
        self.elems = []

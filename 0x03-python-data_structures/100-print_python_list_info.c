#include <Python.h>
/**
 * print_python_list_info - C function that prints some basic
 * info about Python lists.
 * @p: Python Object
 * Return: python lists
 */
void print_python_list_info(PyObject *p)
{
        PyObject *obj;
        int size, allocate, a;

        size = Py_SIZE(p);
        allocate = ((PyListObject *)p)->allocated;
        printf("[*] Size of the Python List = %d\n", size);
        printf("[*] Allocated = %d\n", allocate);

        for (a = 0; a < size; a++)
        {
                printf("Element %d: ", a);
                obj = PyList_GetItem(p, a);
                printf("%s\n", Py_TYPE(obj)->tp_name);
        }
}

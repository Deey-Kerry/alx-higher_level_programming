#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
/**
 * print_python_bytes - a function that prints bytes
 * @p: python object
 * Return: python bytes
 */
void print_python_bytes(PyObject *p)
{
	long int size;
	char *trying_str = NULL;
	int a;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	PyBytes_AsStringAndSize(p, &trying_str, &size);

	printf("  size: %li\n", size);
	printf("  trying string: %s\n", trying_str);
	if (size < 10)
		printf("  first %li bytes:", size + 1);
	else
		printf("  first 10 bytes:");
	for (a = 0; a <= size && a < 10; a++)
		printf(" %02hhx", trying_str[a]);
	printf("\n");
}
/**
 * print_python_list - a function that prints lists
 * @p: python object
 * Return: python lists
 */
void print_python_list(PyObject *p)
{
        PyListObject *list = (PyListObject *)p;
        const char *type;
	long int size = PyList_Size(p);
        int a;

        printf("[*] Python list info\n");
        printf("[*] Size of the Python List = %li\n", size);
        printf("[*] Allocated = %li\n", list->allocated);
        for (a = 0; a < size; a++)
        {
                type = (list->ob_item[a])->ob_type->tp_name;
		printf("Element %i: %s\n", a, type);
                if (!strcmp(type, "bytes"))
                        print_python_bytes(list->ob_item[a]);
        }
}

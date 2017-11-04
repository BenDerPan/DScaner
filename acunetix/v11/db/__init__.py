from psycopg2.extensions import adapt as sql_escape
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.sql.expression import ColumnClause

class FunctionWrapper(ColumnClause):

    def params(self, *optional_dict, **kwargs):
        pass

    def unique_params(self, *optional_dict, **kwargs):
        pass

    def __init__(self, *args, **kwargs):
        self.kwargs = kwargs
        super().__init__(kwargs)


@compiles(FunctionWrapper)
def __compile_function_wrapper(element, compiler, **kw):
    s = ','.join(('%s:=%s' % (k, sql_escape(v)) for k, v in element.kwargs.items()))
    return '%s(%s)' % (element.name, s)
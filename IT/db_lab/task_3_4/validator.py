
class TypeValidator:
    @staticmethod
    def validate(value, field_type):
        if field_type is None:
            raise ValueError("Field type cannot be None.")
        
        if field_type == 'integer':
            return TypeValidator.validate_integer(value)
        elif field_type == 'real':
            return TypeValidator.validate_real(value)
        elif field_type == 'char':
            return TypeValidator.validate_char(value)
        elif field_type == 'string':
            return TypeValidator.validate_string(value)
        else:
            raise ValueError(f"Unsupported field type '{field_type}'")

    @staticmethod
    def validate_integer(value):
        if isinstance(value, int):
            return True
        if isinstance(value, str):
            try:
                int(value)
                return True
            except ValueError:
                return False
        return False

    @staticmethod
    def validate_real(value):
        if isinstance(value, (int, float)):
            return True
        if isinstance(value, str):
            try:
                float(value)
                return True
            except ValueError:
                return False
        return False

    @staticmethod
    def validate_char(value):
        return isinstance(value, str) and len(value) == 1

    @staticmethod
    def validate_string(value):
        return isinstance(value, str)

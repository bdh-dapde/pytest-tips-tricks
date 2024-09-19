def my_name(name):
    """Introduce yourself."""
    # import ipdb;ipdb.set_trace()
    return f"My name is: {name}"


def your_name(name):
    """Greet someone else"""
    return f"Nice to meet you, {name}"

# https://stackoverflow.com/questions/65592626/how-to-test-if-name-main-to-increase-coverage

if __name__ == "__main__": # pragma: no cover
    print(my_name("bob"))

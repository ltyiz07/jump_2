lorem = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin nisl est, aliquet id tincidunt at, venenatis feugiat turpis. Ut varius risus a enim euismod, aliquam malesuada ipsum vestibulum. Maecenas a quam faucibus, pharetra tortor nec, faucibus leo. Ut non rhoncus nulla. Aliquam erat volutpat. Nam quis ultrices nulla, sit amet finibus mi. Nullam a bibendum sapien, sit amet consequat tellus.

Mauris a felis id est tincidunt vehicula dictum eu enim. Nunc consequat lectus erat. Proin libero est, pharetra non ante in, volutpat imperdiet lorem. Suspendisse cursus massa eget nulla pulvinar, eu ultricies augue venenatis. Curabitur gravida sollicitudin mauris sit amet semper. Etiam tincidunt, velit nec aliquam hendrerit, orci ipsum mattis massa, non scelerisque justo tortor vitae orci. Pellentesque ultrices lacus vitae nibh blandit placerat. Curabitur semper mollis tempor. Mauris in fringilla elit, malesuada suscipit risus. Cras viverra rhoncus tincidunt. In a vestibulum ante. Nam fermentum venenatis lorem in tempus. Duis dui mi, lacinia vel tellus elementum, semper bibendum dui. Donec condimentum arcu odio, at laoreet tortor pretium viverra."""
count = 0
re_count = 0
for i in lorem:
    count = count + 1
    if i == 'r':
        if lorem[count] == 'e':
            print("RE found")
            re_count = re_count + 1
print(re_count)
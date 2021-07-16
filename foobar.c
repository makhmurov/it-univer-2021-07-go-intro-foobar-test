#include <stdint.h>
#include <stdio.h>
#include <errno.h>

const char msg_foo[] = "Foo";
const char msg_bar[] = "Bar";

static void foo_bar(uint32_t maximum, uint32_t counter)
{
	if (counter > maximum) return;
	const char *msg = (counter % 3) ? msg_foo : msg_bar;
	printf("%u %s\n", counter, msg);
	++counter;
	foo_bar(maximum, counter);
}

int main(int argc, char* argv[])
{
	int status;
	uint32_t maximum;

	// If run without arguments
	if (argc == 1) {
		puts("Input number greater than 0: ");
		status = scanf("%u", &maximum);
	}
	else {
		status = sscanf(argv[1], "%u", &maximum);
	}
	// WARNING: Unsigned integer overflow not handled
	if (status < 1 || maximum < 1) {
		puts("Incorrect input\n");
		return -1;
	}
	
	foo_bar(maximum, 1);
	
	return 0;
}

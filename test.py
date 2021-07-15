from tinysmpc import VirtualMachine, PrivateScalar, SharedScalar

alice = VirtualMachine("alice")
bob = VirtualMachine("bob")
charlie = VirtualMachine("charlie")

a = PrivateScalar(400, alice)
b = PrivateScalar(150, bob)
c = PrivateScalar(-20, charlie)

print(alice)
print(bob)
print(charlie)

print()
print("Sharing...")
shared_a = a.share([alice, bob, charlie])
print(shared_a)
print()

print(alice)
print(bob)
print(charlie)
print()

print("Adding 500")
shared_a = shared_a + 500
a = shared_a.reconstruct(alice)
print(a)
print()

# Sum = 900 + 150 - 20 = 1030
shared_a = a.share([alice, bob, charlie])
shared_b = b.share([alice, bob, charlie])
shared_c = c.share([alice, bob, charlie])

shared_sum = shared_a + shared_b + shared_c
print("Shared sum =")
# Reconstruct the final sum on Bob's computer
print(shared_sum.reconstruct(bob))
print()

# Lets try out multiplication
shared_a = PrivateScalar(5, alice).share([alice, bob])
shared_b = PrivateScalar(-10, bob).share([alice, bob])

shared_product = 2 * shared_a * shared_b
print("Multiply:")
print(shared_product.reconstruct(alice))


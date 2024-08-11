from some_module import TransactionLock

# Acquire the transaction lock
with TransactionLock():
    # Code that needs to be executed within the transaction lock
    # This ensures that no other code can modify the data being accessed until the lock is released
    # Once the block of code is executed, the lock is automatically released

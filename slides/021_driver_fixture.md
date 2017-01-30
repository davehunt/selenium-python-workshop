# Introducing a driver fixture
In pytest, test functions can receive fixture objects, and each fixture can have its own setup and teardown. This is similar to xUnit style tests, however the setup/teardown is *per fixture*, and fixtures can themselves depend on other fixtures.

If we wanted to add a second test, we'd have to repeat the creation of the `Firefox` object, and if our test failed, the `quit` method will not be called.

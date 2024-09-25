# Django_Assignment
This is a Django Trainee Assignment given by ACCUKNOX

<h3>Are Django signals executed synchronously or asynchronously by default? </h3/>h3>

Django signals are executed synchronously by default. This means that when a signal is triggered, the handler is called immediately, and the execution of the program waits for the signal handler to finish before continuing.

</h3>Do Django signals run in the same thread as the caller by default?</h3>

Yes, by default, Django signals run in the same thread as the caller. Signals are not multi-threaded unless explicitly handled with a background task or threading library.

<h3>Do Django signals run in the same database transaction as the caller by default?</h3>

By default, Django signals can participate in the same database transaction as the caller. If a signal is triggered within a transaction block (like transaction.atomic()), it will be a part of that transaction.

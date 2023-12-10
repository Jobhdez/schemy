# Schemy
Had quite a lot of fun using pattern matching in this little project. 

Nothing serious - just for passing the time

## Usage

```python
>>> from repl import repl 
>>> repl()
lambda> (begin (set! d 3) (+ d 4))
7
lambda> (let ((n 4)) (begin (set! g 5) (set! h 5) (+ n (+ g h))))
14
lambda> (begin (set! d 2) (set! f 4) (+ d f))
6
lambda> (define df (lambda (n) (begin (set! gg 4) (set! ff 4) (+ gg (+ ff n)))))
None
lambda> (df 3)
11
lambda> (let ((ss 4)) (+ ss ss))
8
lambda> (define nn (lambda (n) (let ((f 4)) (begin (set! g 3) (+ f (+ g n))))))
None
lambda> (nn 2)
9
lambda> (list 3 4 5)
(3 4 5)
lambda> (car (list 3 4 5))
3
lambda> (cdr (list 3 4 5))
(4 5)
lambda> (define getfirst (lambda (lst) (car lst)))
lambda> (getfirst (list 3 5 6))
3
lambda> (car (cdr (list 3 4 5)))
4
lambda> (map (lambda (n) (+ n (+ n n))) (list 2 3 4 5))
(6 9 12 15)     
```
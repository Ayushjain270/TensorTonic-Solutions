Input X

(batch=2, T=3, input_dim=4)

        │

        ▼

Time 1 ─────► h1

               │

Time 2 ─────► h2

               │

Time 3 ─────► h3

Store all hidden states:

[

 h1,

 h2,

 h3

]

Shape = (batch, T, hidden_dim)

Only keep the last one:

h_final = h3

Shape = (batch, hidden_dim)
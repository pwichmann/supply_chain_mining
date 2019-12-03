# The code below defines the BiLSTM architecture used in this paper

class LSTM(torch.nn.Module):
    
  # Note that the biDirectional variable is only False in default; we actually pass the value True
  def __init__(self, embedding_mat, d_in, d_out, hidden_size, num_layers, biDirectional = False):
    
    super(LSTM, self).__init__()
    self.hidden_size = hidden_size
    self.directions = 2 if biDirectional else 1
    self.num_layers = num_layers
    self.emb_layer, self.num_embeddings, self.embedding_dim = create_emb_layer(embedding_mat)
    
    # Here we call the torch LSTM module
    self.lstm = torch.nn.LSTM(self.embedding_dim, hidden_size, num_layers=self.num_layers, bidirectional=biDirectional, dropout=0.5)
    
    self.dense = torch.nn.Linear(self.directions*d_in*hidden_size, d_out)
    torch.nn.Dropout()
    self.d_out=d_out

    self.init_state = self.init_hidden(32)


  def init_hidden(self, batch_size):

      # The axes semantics are (num_layers, minibatch_size, hidden_dim)
      #init_h = nn.Parameter(nn.init.xavier_uniform(torch.Tensor(self.num_layers, batch_size, self.hidden_size).type(torch.FloatTensor).cuda()), requires_grad=True)
      #init_c = nn.Parameter(nn.init.xavier_uniform(torch.Tensor(self.num_layers, batch_size, self.hidden_size).type(torch.FloatTensor).cuda()), requires_grad=True)

      #print(init_h.size())
      #print(init_c.size())
      #return (init_h,init_c)

      return (torch.zeros(self.num_layers*self.directions, batch_size, self.hidden_size).to(device),
               torch.zeros(self.num_layers*self.directions, batch_size, self.hidden_size).to(device))


  def forward(self, x):
    bs = len(x)
    x = self.emb_layer(x).view(-1, bs, self.embedding_dim)
    hidden = self.init_hidden(bs)
    output, (hidden, cell) = self.lstm(x, self.init_hidden(bs))
    output = output.view(bs,-1)
    return self.dense(output).view(bs,-1)

  def name(self,optional=""):
      return "{}_lstm_{}_{}".format(str(optional), self.hidden_size, self.d_out)
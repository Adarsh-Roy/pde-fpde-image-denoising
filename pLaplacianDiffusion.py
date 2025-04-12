import torch
from torch_pdegraph.operators import GradMinusInfNorm, GradPlusInfNorm, MeanCurv
from tqdm import tqdm


class PDE(torch.nn.Module):
    def __init__(self, graph, **kwargs):
        super(PDE, self).__init__()
        self.ope_p = GradPlusInfNorm.OPE(graph, **kwargs)
        self.ope_m = GradMinusInfNorm.OPE(graph, **kwargs)
        self.nlm = MeanCurv.OPE(graph, **kwargs)
        self.lamb = kwargs["lamb"]
        self.alpha = kwargs["alpha"]
        self.beta = kwargs["beta"]
        self.edge_index = graph.edge_index
        self.edge_attr = graph.edge_attr

    def forward(self,signal,itr):
        for i in tqdm(range(itr)):
            signal = signal + self.lamb*self.alpha*(self.ope_p(signal)-self.ope_m(signal))*0.5 + self.lamb*self.beta*(self.nlm(signal) - signal)
            # signal = self.nlm(signal)
        return signal
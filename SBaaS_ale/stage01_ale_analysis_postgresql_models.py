from SBaaS_base.postgresql_orm_base import *

class data_stage01_ale_analysis(Base):
    __tablename__ = 'data_stage01_ale_analysis'
    id = Column(Integer, Sequence('data_stage01_ale_analysis_id_seq'), primary_key=True)
    analysis_id = Column(String(500))
    experiment_id = Column(String(50))
    ale_id = Column(String(100))
    analysis_type = Column(String(100)); # time-course (i.e., multiple time points), paired (i.e., control compared to multiple replicates), group (i.e., single grouping of samples).
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (
            UniqueConstraint('experiment_id','ale_id','analysis_type','analysis_id'),
            )
    def __init__(self,data_dict_I):
        self.analysis_id=data_dict_I['analysis_id'];
        self.analysis_type=data_dict_I['analysis_type'];
        self.used_=data_dict_I['used_'];
        self.comment_=data_dict_I['comment_'];
        self.ale_id=data_dict_I['ale_id'];
        self.experiment_id=data_dict_I['experiment_id'];

    def __set__row__(self,analysis_id_I,
                 experiment_id_I,
            ale_id_I,
            analysis_type_I,
            used__I,
            comment__I):
        self.analysis_id=analysis_id_I
        self.experiment_id=experiment_id_I
        self.ale_id=ale_id_I
        self.analysis_type=analysis_type_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
                'analysis_id':self.analysis_id,
            'experiment_id':self.experiment_id,
            'ale_id':self.ale_id,
            'analysis_type':self.analysis_type,
            'used_':self.used_,
            'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())
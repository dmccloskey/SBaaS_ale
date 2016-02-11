from SBaaS_base.postgresql_orm_base import *

class data_stage01_ale_trajectories(Base):
    __tablename__ = 'data_stage01_ale_trajectories'
    id = Column(Integer, Sequence('data_stage01_ale_trajectories_id_seq'), primary_key=True)
    experiment_id = Column(String(50))
    ale_id = Column(String(100))
    ale_time=Column(Float,nullable=False);
    ale_time_units=Column(String(50))
    generations=Column(Float)
    ccd=Column(Float) #cumulative cell divisions
    rate = Column(Float)
    rate_units = Column(String(50))
    used_ = Column(Boolean)
    comment_ = Column(Text);

    __table_args__ = (UniqueConstraint('experiment_id','ale_id','ale_time','ale_time_units','rate_units'),
            )
    def __init__(self,data_dict_I):
        self.ale_id=data_dict_I['ale_id'];
        self.ale_time=data_dict_I['ale_time'];
        self.ale_time_units=data_dict_I['ale_time_units'];
        self.generations=data_dict_I['generations'];
        self.ccd=data_dict_I['ccd'];
        self.rate=data_dict_I['rate'];
        self.rate_units=data_dict_I['rate_units'];
        self.comment_=data_dict_I['comment_'];
        self.used_=data_dict_I['used_'];
        self.experiment_id=data_dict_I['experiment_id'];

    def __set__row__(self,
            experiment_id_I,
            ale_id_I,
            ale_time_I,
            ale_time_units_I,
            generations_I,
            ccd_I,
            rate_I,
            rate_units_I,
            used__I,
            comment__I):
        self.experiment_id=experiment_id_I
        self.ale_id=ale_id_I
        self.ale_time=ale_time_I
        self.ale_time_units=ale_time_units_I
        self.generations=generations_I
        self.ccd=ccd_I
        self.rate=rate_I
        self.rate_units=rate_units_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'experiment_id':self.experiment_id,
                'ale_id':self.ale_id,
                'ale_time':self.ale_time,
                'ale_time_units':self.ale_time_units,
                'generations':self.generations,
                'ccd':self.ccd,
                'rate':self.rate,
                'rate_units':self.rate_units,
                'used_':self.used_,
                'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())

class data_stage01_ale_jumps(Base):
    __tablename__ = 'data_stage01_ale_jumps'
    id = Column(Integer, Sequence('data_stage01_ale_jumps_id_seq'), primary_key=True)
    experiment_id = Column(String(50), primary_key=True)
    ale_id = Column(String(100))
    jump_region_start = Column(Float)
    jump_region_stop = Column(Float)
    used_ = Column(Boolean)
    comment_ = Column(Text);
    def __init__(self,data_dict_I):
        pass;
    def __set__row__(self,experiment_id_I,
            ale_id_I,
            ale_time_I,
            ale_time_units_I,
            rate_fitted_I,
            rate_fitted_units_I,
            jump_region_I,
            used__I,
            comment__I):
        self.experiment_id=experiment_id_I
        self.ale_id=ale_id_I
        self.ale_time=ale_time_I
        self.ale_time_units=ale_time_units_I
        self.rate_fitted=rate_fitted_I
        self.rate_fitted_units=rate_fitted_units_I
        self.jump_region=jump_region_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'experiment_id':self.experiment_id,
                'ale_id':self.ale_id,
                'ale_time':self.ale_time,
                'ale_time_units':self.ale_time_units,
                'rate_fitted':self.rate_fitted,
                'rate_fitted_units':self.rate_fitted_units,
                'jump_region':self.jump_region,
                'used_':self.used_,
                'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())

class data_stage01_ale_stocks(Base):
    __tablename__ = 'data_stage01_ale_stocks'
    id = Column(Integer, Sequence('data_stage01_ale_stocks_id_seq'), primary_key=True)
    experiment_id = Column(String(50))
    ale_id = Column(String(100))
    sample_name_abbreviation = Column(String(100))
    time_point=Column(String(10));
    ale_time=Column(Float,nullable=False);
    ale_time_units=Column(String(50))
    used_ = Column(Boolean)
    comment_ = Column(Text);

    __table_args__ = (UniqueConstraint('experiment_id','ale_id','sample_name_abbreviation','time_point','ale_time','ale_time_units'),
            )
    def __init__(self,data_dict_I):
        self.ale_id=data_dict_I['ale_id'];
        self.sample_name_abbreviation=data_dict_I['sample_name_abbreviation'];
        self.used_=data_dict_I['used_'];
        self.ale_time=data_dict_I['ale_time'];
        self.comment_=data_dict_I['comment_'];
        self.time_point=data_dict_I['time_point'];
        self.ale_time_units=data_dict_I['ale_time_units'];
        self.experiment_id=data_dict_I['experiment_id'];


    def __set__row__(self,
            experiment_id_I,
            ale_id_I,
            sample_name_abbreviation_I,
            time_point_I,
            ale_time_I,
            ale_time_units_I,
            used__I,
            comment__I):
        self.experiment_id=experiment_id_I
        self.ale_id=ale_id_I
        self.ale_time=ale_time_I
        self.ale_time_units=ale_time_units_I
        self.time_point=time_point_I
        self.sample_name_abbreviation=sample_name_abbreviation_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'experiment_id':self.experiment_id,
                'ale_id':self.ale_id,
                'ale_time':self.ale_time,
                'ale_time_units':self.ale_time_units,
                'time_point':self.time_point,
                'sample_name_abbreviation':self.sample_name_abbreviation,
                'used_':self.used_,
                'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())
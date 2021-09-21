import sys

models_paths = {
    'base_unit': 'src.db.models.base.BaseUnit.BaseUnit',
    'prop': 'src.db.models.base.Prop.Prop',
    'unit': 'src.db.models.base.Unit.Unit',

    'material': 'src.db.models.material.Material.Material',
    'material_category': 'src.db.models.material.MaterialCategory.MaterialCategory',
    'material_group': 'src.db.models.material.MaterialGroup.MaterialGroup',
    'material_subgroup': 'src.db.models.material.MaterialSubgroup.MaterialSubgroup',

    'base_volume': 'src.db.models.project.BaseVolume.BaseVolume',
    'equipment': 'src.db.models.project.Equipment.Equipment',
    'estimate': 'src.db.models.project.Estimate.Estimate',
    'project': 'src.db.models.project.Project.Project',

    'city': 'src.db.models.provider.City.City',
    'product': 'src.db.models.provider.Product.Product',
    'provider': 'src.db.models.provider.Provider.Provider',

    'work': 'src.db.models.work.Work.Work',
    'work_group': 'src.db.models.work.WorkGroup.WorkGroup',
    'work_material': 'src.db.models.work.WorkMaterial.WorkMaterial',
    'work_stage': 'src.db.models.work.WorkStage.WorkStage',
    'work_technology': 'src.db.models.work.WorkTechnology.WorkTechnology'
}


def get_model_by_name(name):
    model_path = models_paths.get(name)
    if model_path is None:
        return model_path
    return load_class(model_path)


def load_class(s):
    path, klass = s.rsplit('.', 1)
    __import__(path)
    mod = sys.modules[path]
    return getattr(mod, klass)

import { Module, forwardRef } from "@nestjs/common";
import { AuthModule } from "../auth/auth.module";
import { AddressModuleBase } from "./base/address.module.base";
import { AddressService } from "./address.service";
import { AddressController } from "./address.controller";
import { AddressResolver } from "./address.resolver";

@Module({
  imports: [AddressModuleBase, forwardRef(() => AuthModule)],
  controllers: [AddressController],
  providers: [AddressService, AddressResolver],
  exports: [AddressService],
})
export class AddressModule {}
